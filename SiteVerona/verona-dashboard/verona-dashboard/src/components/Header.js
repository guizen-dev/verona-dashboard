import React from 'react';
import './Header.css'
import logoimg from '../assets/logo.png'

export default function Header(){

    return(
        <div className='header-bg'>
            <div className='logo'>
                <img src={logoimg}/>
            </div>
            <div>
                <h1>
                    Dashboard de clientes
                </h1>
            </div>
        </div>
    )
}