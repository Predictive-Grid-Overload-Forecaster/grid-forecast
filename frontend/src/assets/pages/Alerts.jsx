import React, { use, useEffect, useState } from "react";

const Alerts = ({ alertsfrombackend }) => {
    const criticalmsg = "critical";
    const warningmsg = "warning";
    const resolvedmsg = "resolved";

    const [Alerts, SetAlerts] = useState({
        type : "",
        about : "",
        time : "",
        zone : "",
        color : ""
    })

    const [Area, setArea] = useState("");
    const [Date, setDate] = useState("");

    const [Critical, SetCritical] = useState([]);
    const [Warning, SetWarning] = useState([]);
    const [Resolved, SetResolved] = useState([]);

    useEffect(() => {
        const firstfive = alertsfrombackend.slice(0,5)
        firstfive.map((e,i) => {
            if(e.alerttype == "critical"){
                return{...Alert, color:"yellow"};
            }
            else if(e.alerttype == "warning"){
                return{...Alerts, color:"red"};
            }
            else {
                return{...Alerts, color:'green'}
            }
        })
    }, [Alerts]);

    return (
        <div>
            <div>
                <div>
                    <h1>Live Alert & Notification</h1>
                    <div>
                        <div>
                            <label >Severnity</label>
                            <select>
                                <option>All Severnity</option>
                                <option>Critical</option>
                                <option>Warning</option>
                                <option>Resolved</option>
                            </select>
                        </div>
                        <div>
                            <label>Zone</label>
                            <select onChange={(e) => { setArea(e.target.value) }}>
                                <option value="AllArea">All Area</option>
                                <option value="NorthDelhi">North Delhi</option>
                                <option value="SouthDelhi">South Delhi</option>
                                <option value="EastDelhi">East Delhi</option>
                                <option value="WestDelhi">West Delhi</option>
                                <option value="CentralDelhi">Central Delhi</option>
                                <option value="North-EastDelhi">North-East Delhi</option>
                                <option value="North-WestDelhi">North-West Delhi</option>
                                <option value="South-West Delhi">South-West Delhi</option>
                            </select>
                        </div>
                        <div>
                            <label>Date</label>
                            <input type="date" onChange={(e) => { setDate(e.target.value) }} />
                        </div>
                    </div>
                </div>

                <div>
                    <div>
                        {Alerts.map((alert, i) => {
                            <div className={`bg-${alert.color}`} key={i}>
                                <div>
                                    <h3>{alert.type}</h3>
                                    <p>{alert.time}</p>
                                </div>
                                <p>{alert.about}</p>
                                <p>{alert.zone}</p>
                            </div>
                        })}
                    </div>
                </div>
                <div>
                    <div></div>
                </div>
            </div>
        </div>
    )
};

export default Alerts;
