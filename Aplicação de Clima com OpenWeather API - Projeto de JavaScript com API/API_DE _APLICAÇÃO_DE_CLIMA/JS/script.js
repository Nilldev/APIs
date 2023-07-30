
//variáveis e seleção de elementos
const apikey = "917eb184c7281cf87387fce81df06430";
const cityInput = document.querySelector("#city-input");
const searchBtn = document.querySelector("#search");

const cityElement = document.querySelector("#city");
const tempElement= document.querySelector("#temperature span");
const descElement = document.querySelector("#description");
const weatherIconElement = document.querySelector("#weather-icon");
const countryElement = document.querySelector("#country");
const umidityElement = document.querySelector("#umidity span");
const windElement = document.querySelector("#wind span");

//funções

const getWeatherData = async(city) =>{
  
    const apiWeatherURL = 'https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apikey}&lang=pt_br}'
     const rest = await fetch(apiWeatherURL);
     const data = await rest.json();

     return data

    
};



const showWeatherData= async (city) =>{

    const data =getWeatherData (city);


      cityElements.innerText = data.name;
      tempElement.innerText = parseInt(data.main.temp)
      descElement.innerText = data.weather[0].description;
      weatherIconElement.setAttribute
};

//eventos
searchBtn.addEventListener("click",(e)=>{

e.preventDefault();

const city = cityInput.value;
showWeatherData(city);


});





