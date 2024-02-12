const express = require('express');
const bodyParser = require('body-parser');
const port = 1109;

const app = express();
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }));

const fs = require('fs');
const uuid = require('uuid');

app.get('/getImage'), async (req, res) => {
    img_files = fs.readdirSync('../music_score/raw_images/');
    res.json({ 'img_file': img_files[0] })
}

app.post('/generateLabel'), async (req, res) => {
    // change file location
    img_uuid = uuid.uuid();
    fs.copyFileSync(`../music_score/raw_images/${req.body['img_file']}`, `../music_score/labelled_images/${img_uuid}.png`);
    fs.rmSync(`../music_score/raw_images/${req.body['img_file']}`);
    
    // get latest id
    last_id = fs.readFileSync('../music_score/label.csv').split("\n")[-1].split(",")[0]
    if 
    for (chord in req.body['labels']) {

    }
    label_id = len(fs.readdirSync('../music_score/labelled_images/'));
    label_str = label_id + ',' + img_uuid + ',' + 
}

app.listen(port, () => {
    console.log(`Server listening on port ${port}`)
});