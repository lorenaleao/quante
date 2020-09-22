import React from 'react';
import {TouchableOpacity, View, Text, StyleSheet} from 'react-native';
import {MaterialIcons} from '@expo/vector-icons'

function Main({navigation}){
    return( 
    <View style={styles.principal}>
        <TouchableOpacity style={styles.box}
          onPress={() => navigation.navigate('Login')}>
          <Text style={styles.text}>LOGIN</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.box}
          onPress={() => navigation.navigate('Cadastrar Usuário')}
        >
        <Text style={styles.text}>CADASTRAR USUÁRIO</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.box}
          onPress={() => navigation.navigate('Cadastrar Estabelecimento')}
        >
          <Text style={styles.text}>CADASTRAR        LOJA/MERCADO</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.box}
          title="Cadastrar Produto"
          onPress={() => navigation.navigate('Cadastrar Produto')}
        >
          <Text style={styles.text}>CADASTRAR PRODUTO</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.box}
          title="Perfil de Usuário"
          onPress={() => navigation.navigate('Perfil')}
        >
          <Text style={styles.text}>PERFIL</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.box}
          title="Pesquisar Produto"
          onPress={() => navigation.navigate('Pesquisar')}
        >
          <Text style={styles.text}>PESQUISAR PRODUTO</Text>
        </TouchableOpacity>
    </View>
    );
}

const styles = StyleSheet.create({
  principal:{
    width: '100%',
    height:'100%',
    flexDirection: 'row', 
    flexWrap: 'wrap', 
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: '4%'
  },
  box:{
    width: '45%',
    height: '30%',
    backgroundColor: '#1e5bc6',
    justifyContent: 'center',
    alignItems: 'center',
    margin: 5
  },
  text:{
    fontSize: 20,
    color: 'white',
    textAlign: 'center'
  }
})

export default Main;