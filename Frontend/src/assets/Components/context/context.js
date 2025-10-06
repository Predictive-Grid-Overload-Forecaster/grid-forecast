import React, { useContext } from 'react';
import DataContext from './path/to/context';

const YourComponent = () => {
    const { data, loading, error } = useContext(DataContext);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div>
            {/* Use your data here */}
            {JSON.stringify(data)}
        </div>
    );
};