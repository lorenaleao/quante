import React from 'react';
import {Button, View} from 'react-native';

function Main({navigation}){
    return( 
    <View>
        <Button
          title="Login"
          onPress={() => navigation.navigate('Login')}
        />
        <Button
          title="Cadastrar Usuário"
          onPress={() => navigation.navigate('Cadastrar Usuário')}
        />
        <Button
          title="Cadastrar Estabelecimento"
          onPress={() => navigation.navigate('Cadastrar Estabelecimento')}
        />
        <Button
          title="Cadastrar Produto"
          onPress={() => navigation.navigate('Cadastrar Produto')}
        />
        <Button
          title="Perfil de Usuário"
          onPress={() => navigation.navigate('Perfil')}
        />
        <Button
          title="Pesquisar Produto"
          onPress={() => navigation.navigate('Pesquisar')}
        />
    </View>
    );
}

export default Main;