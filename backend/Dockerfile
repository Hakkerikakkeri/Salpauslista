# Use a Node.js base image with a specified version
FROM node:16

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json separately to leverage Docker caching
COPY package*.json ./

# Install backend dependencies
RUN npm install --production

# Copy the rest of the source code
COPY . .

# Expose the port your backend will run on (adjust as needed)
EXPOSE 3001

# Define the command to run your backend
CMD ["npm", "start"]