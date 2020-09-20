import React from 'react';
import {Button, View} from 'react-native';

function Main({navigation}){
    return( 
    <View>
        <Button
        title="Pesquisar Produto"
        onPress={() => navigation.navigate('Pesquisar')}
      />
    </View>
    );
}

export default Main;