FROM eclipse-temurin:11-jre
WORKDIR /app
COPY build/jar/Lab-4.jar /app/app.jar
CMD ["java", "-jar", "app.jar"]