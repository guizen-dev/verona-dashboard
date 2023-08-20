import React, { useState } from 'react';
import axios from 'axios';
import './Body.css';

export default function Body() {
    const [showClients, setShowClients] = useState(false);
    const [clients, setClients] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    const fetchClients = async () => {
        try {
            setIsLoading(true);
            const response = await axios.get('https://verona-clientes-api.onrender.com/clientes/');
            setClients(response.data);
            setShowClients(true);
        } catch (error) {
            console.error('Error fetching clients:', error);
        } finally {
            setIsLoading(false);
        }
    };

    const convertToCSV = () => {
        const headers = Object.keys(clients[0]).toString();
        const main = clients.map(item => {
            return Object.values(item).toString();
        });
        const csv = [headers, ...main].join('\n');
        downloadCSV(csv);
    };

    const deleteClient = async (id) => {
        try {
            setIsLoading(true);
            await axios.delete(`https://verona-clientes-api.onrender.com/clientes/`);
            const response = await axios.get('https://verona-clientes-api.onrender.com/clientes/');
            setClients(response.data);
        } catch (error) {
            console.error('Error deleting client:', error);
        } finally {
            setIsLoading(false);
        }
    };

    const downloadCSV = input => {
        const blob = new Blob([input], { type: 'application/csv' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.download = 'clientes.csv';
        a.href = url;
        a.style.display = 'none';
        document.body.appendChild(a);
        a.click();
        a.remove();
        URL.revokeObjectURL(url);
    };

    return (
        <div className='body-container'>
            <button className='view-btn' onClick={fetchClients}>
                Visualizar clientes
            </button>

            {isLoading ? (
                <i className="fa-solid fa-spinner fa-spin"></i>
            ) : showClients ? (
                clients.length > 0 ? (
                    <div className='clients-list'>
                        <h2>Lista de clientes</h2>
                        <ul>
                            {clients.map((client, index) => (
                                <li key={index}>
                                    <strong>Name:</strong> {client.name}<br />
                                    <strong>Email:</strong> {client.email_address}<br />
                                    <strong>Phone:</strong> {client.phone_number}
                                </li>
                            ))}
                        </ul>
                        <div className='bottom-div'>
                            <button onClick={convertToCSV} className='csv-btn'>Transformar em .csv</button>
                            <button 
                            onClick={() => deleteClient()} className='delete-btn'>
                                Deletar clientes
                            </button>
                        </div>
                    </div>
                ) : (
                    <h4>
                        Nenhum dado adicionado
                    </h4>
                )
            ) : null}
        </div>
    );
}
