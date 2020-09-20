import React from 'react';
import {Button, View} from 'react-native';

function Main({navigation}){
    return( 
    <View>
        <Button
        title="TELA VERMELHA"
        color={"#e81e26"}
        onPress={() => navigation.navigate('Teste A')}
      />
      <Button
        title="TELA VERDE"
        color={"#2aac00"}
        onPress={() => navigation.navigate('Teste B')}
      />
    </View>
    );
}

export default Main;