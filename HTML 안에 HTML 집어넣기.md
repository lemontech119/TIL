## HTML 안에 HTML 집어넣기

header와 footer 같은 모든 페이지에 중복으로 들어가는 html 코드를 줄이기 위해 html 안에 html집어넣는 법 정리

#### index 페이지

```html
<html>
<head>
 <title>Include Sample</title>

 <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
 <script type="text/javascript" src="includeHtml.js"></script>
 <script type="text/javascript">
  function headerCompleted() {
   $("#sample").html("haha");
  }
  function footerCompleted() {
   $("#sample2").html("hoho");
  }
 </script>
</head>
<body>
 <!-- "include-html" 태그의 "target" 속성에 대치시킬 파일을 지정해준다. -->
 <include-html target="header.html" completed="headerCompleted"></include-html>
 <div>Contents</div>
 <include-html target="footer.html" completed="footerCompleted"></include-html>

 <script>includeHtml();</script>
</body>
</html>
```

#### header 부분 (header.html)

``` html
<div>Header</div>
<div id="sample"></div>
```

#### footer 부분 (footer.html)

``` html
<div>Footer</div>
<div id="sample2"></div>
```

#### index안에 header와 footer를 넣기 위한 js파일

#### includeHtml.js

```javascript
function includeHtml() {
 $("include-html").each(function() {
  element = $(this);
  element.load(element.attr("target"), eval(element.attr("completed")));
 });
}
```



위와 같은 방식으로 집어넣을 수 있지만, 크롬 환경에서는 따로 환경 설정을 해야되기 때문에 서버로 테스트 하면 됩니다.