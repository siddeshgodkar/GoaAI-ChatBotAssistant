# Stage 1: Build React app
FROM node:20 AS build

WORKDIR /app

# Install deps
COPY package*.json ./
RUN npm install

# Copy source
COPY . ./

# Build React app (creates dist/)
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

# Copy built dist into nginx
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
