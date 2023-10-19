import React, { useState } from 'react';
import './../styles/WeatherForecast.css';

function WeatherForecast() {
  const [location, setLocation] = useState(''); // Use an empty string as the initial location
  const [weatherData, setWeatherData] = useState([]);
  const [error, setError] = useState(null);

  const handleGenerateForecast = () => {
    fetchData(); // Trigger fetching data when the button is clicked
  };

  const fetchData = async () => {
    try {
      const response = await fetch(`http://localhost:8000/weather/${location}`);
      if (response.ok) {
        const data = await response.json();
        setWeatherData(data);
        setError(null); // Clear any previous errors
      } else {
        setError('Failed to fetch weather data.');
      }
    } catch (error) {
      setError('An error occurred while fetching weather data.');
    }
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
        };
      }
      groupedData[date].min_temperature.push(forecast.min_temperature);
      groupedData[date].max_temperature.push(forecast.max_temperature);
      groupedData[date].precipitation_sum.push(forecast.precipitation_sum);
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
            <td>Min Temperature</td>
            {dates.map((date) => (
              <td key={date}>
                {groupedData[date].min_temperature.join(', ')}
              </td>
            ))}
          </tr>
          <tr>
            <td>Max Temperature</td>
            {dates.map((date) => (
              <td key={date}>
                {groupedData[date].max_temperature.join(', ')}
              </td>
            ))}
          </tr>
          <tr>
            <td>Total Precipitation</td>
            {dates.map((date) => (
              <td key={date}>
                {groupedData[date].precipitation_sum.join(', ')}
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
      <input
        type="text"
        placeholder="Enter City"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
      />
      <button onClick={handleGenerateForecast}>Generate Forecast</button>
      {error && <p className="error">{error}</p>}
      <div className="table-container">{renderTable()}</div>
    </div>
  );
}

export default WeatherForecast;
