const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const port = 1109;

const app = express();
app.use(cors({
    origin: 'http://127.0.0.1:5500'
}));
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }));

const fs = require('fs');
const uuid = require('uuid');

app.get('/getImage', async (req, res) => {
    const img_files = fs.readdirSync('../music_score/raw_images/');
    res.json({ 'img_file': '../music_score/raw_images/' + img_files[0] });
});

app.post('/generateLabel', async (req, res) => {
    console.log(JSON.stringify(req.body))
    let img_path = req.body.image.split('/');
    img_path = '../music_score/raw_images/' + img_path[img_path.length - 1]
   
    console.log(img_path)
    // change file location
    const img_uuid = uuid.v4()
    fs.copyFileSync(`../music_score/raw_images/${req.body.content}`, `../music_score/labelled_images/${img_uuid}.png`);
    fs.rmSync(`../music_score/raw_images/${req.body['img_file']}`);
    
    // get latest id
    let last_id = fs.readFileSync('../music_score/label.csv').split("\n")[-1].split(",")[0];
    last_id = (last_id == 'ID' ? -1 : Number(last_id));
    // generate label
    for (chord in req.body['labels']) {
        last_id ++;
        let label_str = String(last_id) + ',' + img_uuid + ',' + String(chord+1) + ',' + req.body['x'] + ',' + req.body['duration'] + ',' + req.body['pitch0'] + ',' + req.body['pitch1'] + req.body['pitch2'] + req.body['pitch3'] + req.body['pitch4'] + '\n';
        fs.appendFileSync('../music_score/label.csv', label_str)
    } 
})

app.listen(port, () => {
    console.log(`Server listening on port ${port}`)
});