FROM nginx:alpine

# Create a simple index file
RUN echo "<h1>Hello from my automated GitOps world!</h1>" > /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80
