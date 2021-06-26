const input = document.querySelector('.marca');
const input2 = document.querySelector('.modelo');
const input3 = document.querySelector('.año');
const button = document.querySelector('button2');
const imagen = document.querySelector('.traer');

button2.addEventListener('click', (e) => {
    e.preventDefault();
    traer(input.value, input2.value, input3.value);

})
function traer(marca, model, año){        
    fetch(`https://api.carsxe.com/images?key=albv3qkt1_so8tpezkl_466keecr9&make=${marca}&model=${model}&year=${año}&format=json`)
    .then (response => response.json())
    .then (data =>{
        crearimg(data);
    })
}
function crearimg(auto){
    const img = document.createElement('img');
    img.id = "img1" ; img.src = auto.images['0'].link;   

    const div = document.createElement('div');
    div.append(img);   

    imagen.append(div);
} 

