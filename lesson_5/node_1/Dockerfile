FROM node:alpine
WORKDIR /
COPY package*.json ./
RUN npm install
COPY app.js .
CMD [ "node", "app.js" ]