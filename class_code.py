import requests

# cat_url = 'http://placekitten.com/200/300'
# response = requests.get(cat_url)
# with open('kitten.jpg', 'wb') as file:
#     for chunk in response.iter_content():
#         # iterable content
#         file.write(chunk)

dog_json = requests.get('https://dog.ceo/api/breeds/image/random').json()
img_url = dog_json['message']
image_response = requests.get(img_url)

with open('dog.jpg', 'wb') as file:
    #writing and binary
    for chunk in image_response.iter_content():
       file.write(chunk)
        

