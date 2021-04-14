const express = require('express');
const app = express();
const PORT = 80;

const AWS = require('aws-sdk');
const REGION_NAME = process.env.REGION_NAME;
const BUCKET_NAME = process.env.BUCKET_NAME;

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
                Bucket: BUCKET_NAME
            }

        ).promise();

        if (data) {
            let images = [];
            let promise = await new Promise(function (resolve, reject) {
                data.Contents.forEach(async function (obj, index) {
                    const image = s3.getObject(
                        {
                            Bucket: BUCKET_NAME,
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

    // call async function that retrieves images and diplay them as HTML
    getImageListFromBucket()
        .then((images) => {
            let startHTML = "<html><body><h1>Resized images from '" + BUCKET_NAME + "' bucket</h1></body>";
            let endHTML = "</body></html>";
            let imageHTML = "";
            images.forEach(function (image) {
                imageHTML += "<img src='data:image/jpeg;base64," + encode(image.Body) + "'" + "/>\n";
            });
            let html = startHTML + imageHTML + endHTML;
            res.send(html)
        }).catch((e) => {
            res.send(e)
        })

    function encode(data) {
        let buf = Buffer.from(data);
        let base64 = buf.toString('base64');
        return base64
    }

})

// start the web server
app.listen(PORT, () => {
    console.log(`Web Server running on port ${PORT}`);
});
