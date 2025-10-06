import React, { useEffect, useState } from "react";
import './css/Dashboard/dashboard.css'

const Dashboard = () => {

    const [Energyinmw, SetEnergyinmw] = useState(0)
    const [Difference, SetDifference] = useState("+0%")

    const [Lat, SetLat] = useState(0)
    const [Lon, SetLon] = useState(0)

    const [Temp, SetTemp] = useState(0)
    const [Humidity, setHumidity] = useState(0)
    const [City, SetCity] = useState("")
    const [Date, SetDate] = useState("")
    const [Radiation, SetRadiation] = useState(0)

    return (
        <div className="dashboard">

                {/* this is heading  */}
            <div className="dashboard-header">
                <h1 className="dashboard-title">Dashboard</h1>
                <p className="dashboard-subtitle">Real Time Energy Insight for a Sustainable Future</p>
            </div>

                {/* this is graph section */}
            <div className="dashboard-content">
                <div className="energy-section">
                    <h3 className="section-title">Real Time Energy Demand</h3>
                    <div className="energy-values">
                        <p className="energy-mw">{Energyinmw} MW</p>
                        <p className="energy-diff">{Difference}</p>
                    </div>
                </div>


                <div className="graph-section">
                    <div className="graph-placeholder">
                        Graph
                    </div>
                </div>
            </div>

                {/* this is forecast section  */}
            <div className="forecast-section">
                <h3 className="section-title">Forecast Inputs</h3>

                <div className="input-group">
                    <label className="input-label">City</label>
                    <input className="input-field" value={City} onChange={(e) => SetCity(e.target.value)} type="text" />
                </div>

                <div className="input-group">
                    <label className="input-label">Date</label>
                    <input className="input-field" onChange={(e) => SetDate(e.target.value)} type="date" placeholder="e.g. 1-1-2000" />
                </div>

                <div className="input-group">
                    <label className="input-label">Temperature (°C)</label>
                    <input className="input-field" type="number" value={Temp} onChange={(e) => SetTemp(e.target.value)} />
                </div>

                <div className="input-group">
                    <label className="input-label">Humidity (%)</label>
                    <input className="input-field" type="number" value={Humidity} onChange={(e) => setHumidity(e.target.value)} />
                </div>

                <div className="input-group">
                    <label className="input-label">Radiation (W/m²)</label>
                    <input className="input-field" type="number" value={Radiation} onChange={(e) => SetRadiation(e.target.value)} />
                </div>
            </div>
        </div>
    )
}

export default Dashboard;
