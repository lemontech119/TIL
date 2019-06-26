## HTML에서 Tab쓰는 법

HTML에서는 \t가 따로 먹히지 않는다.

> \<pre>태그를 사용하면 가능하겠지만 그럴 경우 js를 통해서 반복을 할 경우 원하는 대로 값을 못 넣을 확률이 높아진다.
>
> 그렇기에 css문법을 통해 tab을 줘야 한다. 

``` javascript
<script>
	let gugu_sum2;
    for(let i=9; i>=1; i--){
        for(let j=2; j<10; j++){
            gugu_sum2 = i*j;
            document.write(j + " X " + i + " = " + gugu_sum2 +"<span style='white-space:pre'>&#9;</span>");
        }
        document.write("<br>");
    }
</script>

//위의 코드는 탭을 활용하여 구구단 작성 코드이다.
```

> \<span style="white-space:pre">\&\#9;\</span>
>
> style 속성으로 white-space:pre 부여하고 원하는 tab 칸을 \&#9; 숫자 대신 써주면 됨