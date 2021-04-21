FROM node:13-alpine

WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .

EXPOSE 80
CMD [ "node", "index.js" ]
