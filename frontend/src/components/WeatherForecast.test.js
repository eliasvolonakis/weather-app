import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import WeatherForecast from './WeatherForecast';

// Mock fetch to simulate API requests
global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve([]),
    ok: true,
  })
);

describe('WeatherForecast Component', () => {
  test('Renders Without Errors', () => {
    render(<WeatherForecast />);
  });

  test('Handles user input and fetches data', async () => {
    render(<WeatherForecast />);
    const input = screen.getByPlaceholderText('Enter City');
    const generateButton = screen.getByText('Generate Forecast');

    fireEvent.change(input, { target: { value: 'Toronto' } });
    fireEvent.click(generateButton);

    expect(global.fetch).toHaveBeenCalledWith('http://localhost:8000/weather/Toronto');
    expect(screen.getByText('Date')).toBeInTheDocument();
    expect(screen.getByText('Min Temperature (°C)')).toBeInTheDocument();
    expect(screen.getByText('Max Temperature (°C)')).toBeInTheDocument();
    expect(screen.getByText('Feels Like (°C)')).toBeInTheDocument();
    expect(screen.getByText('Total Precipitation (mm)')).toBeInTheDocument();
    expect(screen.getByText('Max UV Index')).toBeInTheDocument();
    expect(screen.getByText('Windspeed (KM/HR)')).toBeInTheDocument();
    expect(screen.getByText('Sunrise')).toBeInTheDocument();
    expect(screen.getByText('Sunset')).toBeInTheDocument();
  });
});
