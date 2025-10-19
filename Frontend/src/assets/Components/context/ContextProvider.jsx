import React, { useEffect, useState } from "react";
import DataContext from "./context";

export const DataProvider = ({ children }) => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                setLoading(true);
                const response = await fetch('YOUR_API_ENDPOINT');
                if (!response.ok) {
                    throw new Error('Failed to fetch data');
                }
                const jsonData = await response.json();
                setData(jsonData);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    return (
        <DataContext.Provider value={{ data, loading, error }}>
            {children}
        </DataContext.Provider>
    );
};

export default DataProvider;