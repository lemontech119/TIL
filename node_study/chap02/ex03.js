function b() {
    console.trace('에러 위치 추적');
 }
 
 function a() {
    b();
 }
 a();
 