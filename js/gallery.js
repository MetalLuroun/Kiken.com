var urlencoded = new URLSearchParams();

var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("http://146.56.199.136:8080/api/picture?page_size=5&page=0", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));

