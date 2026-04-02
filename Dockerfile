FROM nginx:alpine

# Remove the 'RUN echo' line if it's there
# ADD THIS LINE:
COPY index.html /usr/share/nginx/html/index.html
# Expose port 80
EXPOSE 80
