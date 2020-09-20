import * as React from 'react';
import { View, Text } from 'react-native';
import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';

import Main from './pages/Main';
import Teste1 from './pages/Teste1';

const Stack = createStackNavigator();

//Colocar isso no Stack.Navigator pra cor definitiva
/*
screenOptions={{
            headerStyle: { backgroundColor: '#1e5bc6' },
            headerTintColor: '#ffffff',
        }}
*/

function Routes() {
    return (
      <NavigationContainer>
        <Stack.Navigator screenOptions={{
            headerTintColor: '#ffffff',
            headerTitleStyle: {
                fontWeight: 'bold',
            },
        }}>
        <Stack.Screen name="Quanté?" component={Main} options={{
          headerStyle: {
            backgroundColor: '#1e5bc6',
          },
        }}/>
        <Stack.Screen name="Teste A" component={Teste1} options={{
          headerStyle: {
            backgroundColor: '#e81e26',
          },
        }}/>
        <Stack.Screen name="Teste B" component={Teste1} options={{
          headerStyle: {
            backgroundColor: '#2aac00',
          },
        }}/>
        </Stack.Navigator>
      </NavigationContainer>
    );
  }

export default Routes;