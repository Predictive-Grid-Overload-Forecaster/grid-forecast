import React, { useState, useSyncExternalStore } from "react";

const Alerts = () => {

    const [Details, SetDetails] = useState({});

    return (
        <div>
            <div>
                <h1>Live Alerts & Notification</h1>
                <div>
                    <div>
                        <select>
                            <option>All Severnity</option>
                            <option>Crtical</option>
                            <option>Warning</option>
                            <option>Resolved</option>
                        </select>
                    </div>
                    <div>
                        <select>
                            <option>Zone 1</option>
                            <option>Zone 2</option>
                            <option>Zone 3</option>
                        </select>
                    </div>
                    <div>
                        <label>Date</label>
                        <input type="date" placeholder="mm/dd/yyyy" />
                    </div>
                </div>
                <div>
                    example of alert coming from backend will change this in some time

                    add a details button to show the details
                </div>
                <div>
                    <h3>Alert Details</h3>
                    <div>
                        <p>{Details.zone}</p>
                        <p>{Details.Substation}</p>
                        <p>{Details.Affectedzone}</p>
                        <p>{Details.estDuration + "Minutes"}</p>
                        <p>{"Suggested Action :" + Details.Substation + ". Reroute power from " + Details.Extrapowerarea}</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Alerts;