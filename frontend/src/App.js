import React from 'react';
import './App.css';
import WeatherForecast from './components/WeatherForecast';

const appStyle= {
  width: '100vw',
  height: '100vh',
  backgroundImage: `url(${'./../images/sky.png'})`,
  backgroundPosition: 'center',
  backgroundSize: 'cover',
  backgroundRepeat: 'no-repeat',
}

function App() {
  return (
    <div className="App" style={appStyle}>
      <body>
        <WeatherForecast />
      </body>
    </div>
  );
}

export default App;
