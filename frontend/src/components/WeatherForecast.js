import React, { useState } from 'react';
import './../styles/WeatherForecast.css';
import { WiDaySunny, WiCloudy, WiRain, WiDayStormShowers } from 'react-icons/wi';

function WeatherForecast() {
  // Use an empty string as the initial location
  const [location, setLocation] = useState('');
  const [weatherData, setWeatherData] = useState([]);
  const [error, setError] = useState(null);

  const handleGenerateForecast = () => {
    // Trigger fetching data when the button is clicked
    fetchData();
  };

  const fetchData = async () => {
    try {
      // Get backend data
      const response = await fetch(`http://localhost:8000/weather/${location}`);
      if (response.ok) {
        const data = await response.json();
        setWeatherData(data);
        // Clear any previous errors
        setError(null);
      } else {
        setError('Failed to fetch weather data.');
      }
    } catch (error) {
      setError('An error occurred while fetching weather data.');
    }
  };

  const getWeatherIcon = (weatherCode) => {
    weatherCode = Number(weatherCode)
    // Define iconMapping based on WMO weathercode
    const iconMapping = [
        { min: 0, max: 5, icon: <WiDaySunny /> },
        { min: 6, max: 19, icon: <WiCloudy /> }, 
        { min: 20, max: 29, icon: <WiRain /> },
        { min: 30, max: 39, icon: <WiDayStormShowers /> },
        { min: 40, max: 49, icon: <WiCloudy /> },
        { min: 50, max: 94, icon: <WiRain /> },
        { min: 95, max: 100, icon: <WiDayStormShowers /> },
    ];

    const matchedRule = iconMapping.find((rule) => weatherCode >= rule.min && weatherCode <= rule.max);
    return matchedRule ? matchedRule.icon : null;
    };


  const renderTable = () => {
    // Group weather data by date
    const groupedData = {};
    weatherData.forEach((forecast) => {
      const date = forecast.date;
      if (!groupedData[date]) {
        groupedData[date] = {
          min_temperature: [],
          max_temperature: [],
          precipitation_sum: [],
          weathercode: [],
          sunrise: [],
          sunset: [],
          uv_index_max: [],
          windspeed_10m_max: [],
          feels_like: []
        };
      }
      groupedData[date].min_temperature.push(forecast.min_temperature);
      groupedData[date].max_temperature.push(forecast.max_temperature);
      groupedData[date].precipitation_sum.push(forecast.precipitation_sum);
      groupedData[date].weathercode.push(forecast.weathercode);
      groupedData[date].sunrise.push(forecast.sunrise);
      groupedData[date].sunset.push(forecast.sunset);
      groupedData[date].uv_index_max.push(forecast.uv_index_max);
      groupedData[date].windspeed_10m_max.push(forecast.windspeed_10m_max);
      groupedData[date].feels_like.push(forecast.feels_like);      
    });
  

    // Get unique dates for columns
    const dates = Object.keys(groupedData);

    // Render the table
    return (
      <table className="forecast-table">
        <thead>
          <tr>
            <th>Date</th>
            {dates.map((date) => (
              <th key={date}>{date}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          <tr>
            <td></td>
            {dates.map((date) => (
              <td key={date}>
                <span className="icon-large">{getWeatherIcon(groupedData[date].weathercode)}</span>
              </td>
            ))}
          </tr>
          <tr>
            <td>Feels Like (&deg;C)</td>
            {dates.map((date) => (
              <td key={date}>
                {groupedData[date].feels_like.join(', ')}
              </td>
            ))}
          </tr>
          <tr>
            <td>Min Temperature (&deg;C)</td>
            {dates.map((date) => (
              <td key={date}>
                {groupedData[date].min_temperature.join(', ')}
              </td>
            ))}
          </tr>
          <tr>
            <td>Max Temperature (&deg;C)</td>
            {dates.map((date) => (
              <td key={date}>
                {groupedData[date].max_temperature.join(', ')}
              </td>
            ))}
          </tr>
          <tr>
            <td>Total Precipitation (mm)</td>
            {dates.map((date) => (
              <td key={date}>
                {groupedData[date].precipitation_sum.join(', ')}
              </td>
            ))}
          </tr>
          <tr>
            <td>Max UV Index</td>
            {dates.map((date) => (
              <td key={date}>
                {groupedData[date].uv_index_max.join(', ')}
              </td>
            ))}
          </tr>
          <tr>
            <td>Windspeed (KM/HR)</td>
            {dates.map((date) => (
              <td key={date}>
                {groupedData[date].windspeed_10m_max.join(', ')}
              </td>
            ))}
          </tr>
          <tr>
            <td>Sunrise</td>
            {dates.map((date) => (
              <td key={date}>
                {groupedData[date].sunrise.join(', ')}
              </td>
            ))}
          </tr>
          <tr>
            <td>Sunset</td>
            {dates.map((date) => (
              <td key={date}>
                {groupedData[date].sunset.join(', ')}
              </td>
            ))}
          </tr>
        </tbody>
      </table>
    );
  };

  return (
    <div className="WeatherForecast">
    <h1 style={{ fontFamily: 'Georgia', color: 'WhiteSmoke' }}>Weather Forecast</h1>
    <div className="input-container">
      <input
        type="text"
        placeholder="Enter City"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
      />
    </div>
    <button className="rounded-button" onClick={handleGenerateForecast}>
        Generate Forecast
    </button>
    {error && <p className="error">{error}</p>}
    <div className="table-container">{renderTable()}</div>
  </div>
  );
}

export default WeatherForecast;
