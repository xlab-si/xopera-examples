const express = require('express')
const path = require('path');
const app = express()
const multer = require('multer')
const upload = multer()

const AWS = require('aws-sdk');
const PORT = 80;
const REGION_NAME = process.env.REGION_NAME;
const BUCKET_IN_NAME = process.env.BUCKET_IN_NAME;
const BUCKET_OUT_NAME = process.env.BUCKET_OUT_NAME;

function encode(data) {
    let buf = Buffer.from(data);
    let base64 = buf.toString('base64');
    return base64
}

// Set default route
app.get('/', (req, res) => {
    // Set the AWS region
    AWS.config.update({ region: REGION_NAME });
    // Create a new S3 client object
    let s3 = new AWS.S3();

    // function that retrieves all images from S3 bucket and returns a promise with the list of images
    async function getImageListFromBucket() {
        const data = await s3.listObjectsV2(
            {
                Bucket: BUCKET_OUT_NAME
            }

        ).promise();

        if (data) {
            let images = [];
            let promise = await new Promise(function (resolve, reject) {
                data.Contents.forEach(async function (obj, index) {
                    const image = s3.getObject(
                        {
                            Bucket: BUCKET_OUT_NAME,
                            Key: obj.Key
                        }

                    ).promise();

                    images.push(image);
                });
                resolve(images)
            });

            return Promise.all(promise);
        }
    }

    // call async function that retrieves images and displays them as HTML
    getImageListFromBucket()
        .then((images) => {
            let startHTML = "<html><body><h1>Thumbnail generator application (with AWS Lambda and S3 buckets)</h1>";
            let imageUploadHTML = `<form method="POST" action="/upload" enctype="multipart/form-data">
                <div>
                    <label>Upload image to '${BUCKET_IN_NAME}' bucket:</label>
                    <input type="file" name="new_image" />
                    <input type="submit" name="upload_new_image_button" value="Upload" />
                </div>
            </form>
            <h3>Resized images from '${BUCKET_OUT_NAME}' bucket:</h3>`
            let endHTML = "</body></html>";
            let imageHTML = "";

            images.forEach(function (image) {
                imageHTML += "<img src='data:image/jpeg;base64," + encode(image.Body) + "'" + "/>\n";
            });
            let html = startHTML + imageUploadHTML + imageHTML + endHTML;

            res.send(html);
        }).catch((e) => {
            res.send(e);
        })
});

// route for uploading new images to S3 bucket
app.post('/upload', upload.single('new_image'), (req, res) => {
    // 'new_image' is the name of our file input field in the HTML form
    // req.file contains information of uploaded file
    // req.body contains information of text fields, if there were any

    if (req.fileValidationError) {
        return res.send(req.fileValidationError);
    }
    else if (!req.file) {
        return res.send('<h3>Please select an image to upload!</h3><a href="/">Go back to main page</a>');
    }

    // Use S3 ManagedUpload class as it supports multipart uploads
    var upload = new AWS.S3.ManagedUpload({
        params: {
            Bucket: BUCKET_IN_NAME,
            Key: req.file.originalname,
            Body: req.file.buffer
        }
    });

    var promise = upload.promise();

    promise.then(
        function (data) {
            console.log("Successfully uploaded new image.");
        },
        function (err) {
            console.log(req.file);
            console.log(`There was an error uploading image: ${err.message}`);
        }
    );
    res.redirect('/');
});

// start the web server
app.listen(PORT, () => {
    console.log(`Web Server running on port ${PORT}`);
});
