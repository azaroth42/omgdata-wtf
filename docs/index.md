---
title: "OMG, Data... WTF? Egregious Errors in Cultural Heritage Data"

---
# Data Science Group Therapy

## Egregious Data Errors

```crom
top = model.HumanMadeObject(ident="auto int-per-segment", label="Example Object")
top.current_location = model.Place(ident="http://vocab.getty.edu/tgn/7123456", label="Somewhere")
top.dimension = vocab.Height(value=10)
```

## Macro

```crom
top = model.HumanMadeObject(ident="auto int-per-segment", label="Simple Example Painting")
top.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300033618", label="Painting")
top.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300133025", label="Work of Art")
```

