# Use a lightweight web server as the base
FROM nginx:alpine

# Create a simple index file
RUN echo "<h1>Hello from my CI/CD Pipeline!</h1>" > /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Triggering new build with correct permissions
