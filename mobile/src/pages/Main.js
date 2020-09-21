import React from 'react';
import {Button, View} from 'react-native';

function Main({navigation}){
    return( 
    <View>
        <Button
          title="Cadastrar Produto"
          onPress={() => navigation.navigate('CadastrarProduto')}
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