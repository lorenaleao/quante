import * as React from 'react';
import { View, Text } from 'react-native';
import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';

import Main from './pages/Main';
import BuscaProduto from './pages/Busca';
import CadastraProduto from './pages/CadastraProduto';
import PerfilUsuario from './pages/PerfilUsuario';
import Login from './pages/Login'
import CadastraUsuario from './pages/CadastraUsuario'
import CadastraEstabelecimento from './pages/CadastraEstabelecimento'
import Produto from './pages/Produto';
import AtualizaPrecoProduto from './pages/AtualizaPrecoProduto';

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
        <Stack.Screen name="Login" component={Login}/>
        <Stack.Screen name="Quanté?" component={Main}/>
        <Stack.Screen name="Cadastrar Usuário" component={CadastraUsuario}/>
        <Stack.Screen name="Cadastrar Estabelecimento" component={CadastraEstabelecimento}/>
        <Stack.Screen name="Cadastrar Produto" component={CadastraProduto} />
        <Stack.Screen name="Perfil" component={PerfilUsuario} />
        <Stack.Screen name="Pesquisar" component={BuscaProduto} />
        <Stack.Screen name="Produto" component={Produto} />
        <Stack.Screen name="Atualizar Preço" component={AtualizaPrecoProduto} />
        </Stack.Navigator>
      </NavigationContainer>
    );
  }

export default Routes;