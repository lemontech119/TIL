// 여러가지 키워드로 검색된 결과를 1번 저장
const contents = ['cat', 'wow', 'asap', 'coding']
const keyword = contents[Math.floor(Math.random() * contents.length)];

const key = contents[keyword]

function searchTV(key){
    //API 요청
    const URL = `http://api.giphy.com/v1/gifs/search?q=${key}&api_key=${API_KEY}`;

    const GiphyAJAXCall = new XMLHttpRequest();
    GiphyAJAXCall.open('GET', URL);
    GiphyAJAXCall.send();

    GiphyAJAXCall.addEventListener("load", e =>{
        const rawData = e.target.response;
        const parsedData = JSON.parse(rawData);
        console.log(parsedData)
        tvArea(parsedData)
    })
};

// 저장된 값에서 하나씩 꺼내서 보여줌! (랜덤)
const tvAreas = document.querySelector("#js-tv-area")


function tvArea(parsedData){
    const length = parsedData.data.length;
    let ranNum = Math.floor(Math.random() * length);
    const data = parsedData.data
    tvAreas.innerHTML = `<img src="${data[ranNum].images.original.url}" alt="${data[ranNum].title}" />`
    
};

$(document).ready(function(){
    setInterval("searchTV(key)", 3000);
})

document.addEventListener('DOMContentLoaded', searchTV)
