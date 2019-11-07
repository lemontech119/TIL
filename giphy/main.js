const button = document.querySelector("#js-button");
const inputArea = document.querySelector("#js-input");
const resultArea = document.querySelector("#result-area");


// API 요청
function searchAndPush(keyword){
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${API_KEY}`;

    const GiphyAJAXCall = new XMLHttpRequest();
    GiphyAJAXCall.open('GET', URL);
    GiphyAJAXCall.send();

    GiphyAJAXCall.addEventListener("load", e =>{
        const rawData = e.target.response;
        const parsedData = JSON.parse(rawData);
        console.log(parsedData)
        pushToDom(parsedData)
    })

}

// DOM 그리기
function pushToDom(parsedData){
    resultArea.innerHTML = null;
    const dataSet = parsedData.data;
    dataSet.forEach(element => {
        resultArea.innerHTML += `<img src="${element.images.original.url}" alt="${element.title}" />`
    });


}

button.addEventListener("click", ()=>{
    searchAndPush(inputArea.value)
});

button.addEventListener("keypress", e =>{
    if(e.which === 13) searchAndPush(inputArea.value);
});
