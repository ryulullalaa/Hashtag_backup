# HashTag
HashTag is a container image integrity verification system.    
HashTag implements integrity verification by mapping the layer meta information and layer data included in the Docker image with hash values.


<img src="./flowchart.PNG"  width="700" height="370">

# Getting started with Docker
* Crawl docker image   
  ``` docker pull [image name] ```

* Store docker image   
    ``` docker save -o pumevnezdiroorg_img.tar pumevnezdiroorg/drupal ```   
    ``` mkdir pumevnezdiroorg_img ```   
    ``` tar -xvf pumevnezdiroorg_img.tar -C pumevnezdiroorg_img ```

* Compare between base image and downloaded image   
  ``` docker history [image name] ```
  ``` docker inspect drupal:latest | jq '.[].RootFS' ```

* Compare throungh docker container   
  ``` docker run -it -d --name drupal_official drupal:latest ```   
  ``` docker diff drupal_official```

* Parse shellscript   
    ``` docker history --no-trunc ynprpagamentitk/liferay ```
