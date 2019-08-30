## node, express, 몽고DB 에서 페이징

1 단계: 페이징 수가 10개가 넘어가는 경우 고려하지 않고 단순 페이징

``` javascript
let page = req.query.page;
// 몇 페이지인지 데이터 받아오기

if(!page){
    page = 1;
}else{
    page = parseInt(page);
}
// 처음 들어갔을 경우 페이지 값을 못 받아 오기 때문에 값이 없을 경우 1부여
// 기본적으로 받아오는 값이 int가 아니기 때문에 int로 치환

let skip = (page - 1) * 10;
// 페이징을 위한 스킵할 데이터의 수
let limit = 10;
// 한 페이지에 보여줄 데이터의 수

let count_member = await User.count();
// 전체 데이터의 수

let pnTotal = Math.ceil(count_member / limit);
// 페이징 숫자

let all_member = await User.find().skip(skip).limit(limit);
// 보여줄 데이터
```



2 단계: 페이징 수가 10개가 넘어가는 경우 고려 및 마지막 페이지 이동 기능

server

``` javascript
// 위 1단계에서 추가적을 작성

let pnSize = 10;
// 한 번에 보여줄 수 있는 페이징의 숫자 ex) 11까지 있으면 10까지 보여주고 11은 그 다음에

let pnStart = ((Math.ceil(page/pnSize) -1) * pnSize) +1;
// 페이징 시작점

let pnEnd = (pnStart + pnSize) -1;
// 페이징 마지막

if(pnEnd > pnTotal){
    pnEnd = pnTotal;
}
// 전체 페이징 숫자가 페이징 마지막으로 지정하려고 한 값보다 작을 경우 맞춰주기

```



client

``` ejs
<div class="paging">
    <a href="/member?page=<%= page - 1 %>" id="prev" name="<%=page-1%>">
        <i class="fas fa-caret-left"></i>
    </a>
    <% for(let p=pnStart; p <= pnEnd; p++){ %>
    	<a href="/member?page=<%= p %>"> <%= p %> </a> &nbsp;
    <% } %>
    <a href="/member?page=<%= page + 1 %>" id="next" name="<%=page+1%>">
        <i class="fas fa-caret-right"></i>
    </a>
    <a href="/admin/member_manage?page=<%= pnTotal %>">끝</a>
</div>
```



3 단계: 첫 페이징에서 전 페이징으로 버튼과 마지막 페이징에서 다음 페이징으로 버튼 누를 시 데이터 X

``` javascript
<script>
    let prev = $('#prev').attr('name');
    let next = $('#next').attr('name');
    let end = <%= pnTotal %>;
        
    // 현재 페이징이 첫 페이지일 경우
    if (prev == 0) {
        $('#prev').click(function (e) {
            console.log("막아지는거임");
            e.preventDefault();
            // 실행 안되게 막아버림
        });
    }
	// 현재 페이징이 마지막 페이징일 경우
    if(next == end + 1){
        $('#next').click(function (e){
            console.log("막아지는거임2");
            e.preventDefault();
        })
    }
</script>
```

