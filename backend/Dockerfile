FROM node:lts-alpine as base
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
RUN npm i -D
COPY . ./
CMD ["npm", "run", "start"] 