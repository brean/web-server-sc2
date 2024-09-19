FROM node:lts-alpine

WORKDIR /app
ADD ./package*.json ./
ADD ./svelte.config.js ./
ADD ./tsconfig.json ./
ADD ./vite.config.ts ./
ADD ./src/theme/_smui-theme.scss ./src/theme/_smui-theme.scss 
ADD ./src/theme/dark/_smui-theme.scss ./src/theme/dark/_smui-theme.scss 
RUN mkdir ./static
ADD ./.npmrc ./
RUN npm i -D

COPY . ./
RUN npm run smui
CMD npm run dev -- --host