# Cheat Sheet 
Useful stuff for exam


## 02/07/2021


### Interfaces

Un'interfaccia è uno strumento fondamentale del Polimorfismo e della "Composition". L'interfaccia è una struttura che descrive una serie di comportamenti garantiti _(i metodi di un'interfaccia sono pubblici e astratti, quindi vanno sovrascritti)_ che deve implementare la classe che la estende. L'interfaccia è utile a chi sviluppa librerie _(o API in generale)_ per definire che formato devono avere le informazioni che la libreria consuma, ed è utile a chi usufruisce della libreria, perché è uno strumento per adattare le proprie classi / strutture per interagire con l'API. 

Un esempio potrebbe essere:

```java
public interface Serializable {
    public String toJson();
    public Object fromJson(String);
}

public class User implements Serializable {
    // ...

    @Override
    public String toJson() {
        return ...
    }

    @Override
    public Object fromJson(String) {
        return ...
    }
}

public static <T: Serializable> void sendToMongoDB(T object) {
    // ... 

    String content = object.toJson();
}

public static <T: Serializable> T getFromMongoDB(String url) {
    // ... 

    return content.fromJson();
}
```

L'interfaccia `Serializable` permette a chi scrive la libreria di essere sicuro che riceve ogetti convertibili a JSON, e a comunicare a chi usa la libreria che gli ogetti che la libreria consuma devono essere convertibili in JSON, senza a costringere chi usa la libreria a modificare drasticamente la struttura del suo codice, dato che una classe può implementare un numero indeterminato di interfacce. _(JavaScript Object Notation)_
