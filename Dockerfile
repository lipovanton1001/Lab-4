FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY build/jar/Lab-4.jar /app/app.jar
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]