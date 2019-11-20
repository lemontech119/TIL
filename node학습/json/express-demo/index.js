const express = require('express');
const app = express();

app.get('/', (req, res)=>{
    res.send('happy hacking!');
})

app.get('/api/members', (req, res)=>{
    res.send({
        john: "Block Chain",
        tony: "python",
        tak: "Machine Learning",
        zzulu: "Ruby on Rails"
    })
})

const PORT = process.env.PORT || 3000

app.listen(PORT, () => console.log(`${PORT} port open`));