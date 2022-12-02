# PHP protobuf extension issue

## 3.19.4: OK

```
docker build -f DockerfileOK3-19-4 -t php-protobuf-ext-issue . && docker run php-protobuf-ext-issue
```

## \> 3.19.4: KO

```
docker build -f DockerfileKOlatest -t php-protobuf-ext-issue . && docker run php-protobuf-ext-issue
```