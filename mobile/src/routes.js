import * as React from 'react';
import { View, Text } from 'react-native';
import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';

import Main from './pages/Main';
import BuscaProduto from './pages/Busca';
import CadastraProduto from './pages/CadastraProduto';
import CadastrarUsuario from './pages/PerfilUsuario';

const Stack = createStackNavigator();

//Colocar isso no Stack.Navigator pra cor definitiva
/*
screenOptions={{
            
        }}
*/

function Routes() {
    return (
      <NavigationContainer>
        <Stack.Navigator screenOptions={{
            headerStyle: { backgroundColor: '#1e5bc6' },
            headerTintColor: '#ffffff',
            headerTitleStyle: {
                fontWeight: 'bold',
            },
        }}>
        <Stack.Screen name="Quanté?" component={Main}/>
        <Stack.Screen name="CadastrarProduto" component={CadastraProduto} />
        <Stack.Screen name="Perfil" component={CadastrarUsuario} />
        <Stack.Screen name="Pesquisar" component={BuscaProduto} />
        </Stack.Navigator>
      </NavigationContainer>
    );
  }

export default Routes;