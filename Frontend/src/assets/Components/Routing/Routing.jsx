import Navbar from "../../pages/Navbar";
import Dashboard from "../../pages/Dashboard";
import Alerts from "../../pages/Alerts";
import Renewables from "../../pages/Renewables";
import Energy_map from "../../pages/Energy_Map";

import { Routes, Route } from "react-router";
import Help from "../../pages/Help&Support";
import Chatbot from "../../pages/Chatbot";

const AppRoutes = () => {
    return (
        <Routes>
            <Route path="/" element= { <Dashboard /> } />
            <Route path="/Alerts" element={ <Alerts />} />
            <Route path="/Renewables" element={ <Renewables />} />
            <Route path="/Energy_map" element={ <Energy_map />} />
            <Route path="/Help" element={ <Help />} />
            <Route path="/Chatbot" element={ <Chatbot />} />
        </Routes>
    )
}

export default AppRoutes