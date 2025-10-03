FROM node:20-alpine

WORKDIR /app
COPY frontend/package.json frontend/pnpm-lock.yaml* frontend/npm-package-lock.json* /app/
RUN npm i -g pnpm && pnpm install || npm install

COPY frontend /app
EXPOSE 3000
CMD ["npm", "run", "dev"]


