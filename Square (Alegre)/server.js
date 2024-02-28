require('dotenv').config(); 

const express = require('express'); 

const { Client, Environment } = require('@square/square'); 

 

const app = express(); 

const port = 3000; 

 

// Configura el cliente de Square con tu token de acceso 

const squareClient = new Client({ 

  accessToken: process.env.SQUARE_ACCESS_TOKEN, 

  environment: Environment.Sandbox, // Cambia a Environment.Production para producción 

}); 

 

app.use(express.static('public')); // Sirve archivos estáticos desde la carpeta 'public' 

 

// Ruta para verificar la conexión a Square 

app.get('/check-connection', async (req, res) => { 

  try { 

    const response = await squareClient.customersApi.listCustomers(); 

    res.json({ success: true, message: 'Conexión exitosa con la API de Square.' }); 

  } catch (error) { 

    res.json({ success: false, message: 'Falló la conexión con la API de Square.' }); 

  } 

}); 

 

app.listen(port, () => { 

  console.log(`Servidor escuchando en http://localhost:${port}`); 

}); 