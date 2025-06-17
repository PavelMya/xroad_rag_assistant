### 2.2 Represented Parties

The `XRoadRepresentedPartyType` complex type is used to describe represented parties. It consists of two elements: `partyClass` and `partyCode`. The `partyCode` element is mandatory and the `partyClass` element is optional.

```xml

    
        
        
    

```

Next, the elements used in the `XRoadRepresentedPartyType` are defined. Element `partyClass` is similar to the element `memberClass` described in the X-Road Message Protocol 4.0 \[[PR-MESS](#Ref_PR-MESS)\], but can additionally identify institutions that can not become members of X-Road.

Element `partyCode` is used to uniquely identify represented parties.

```xml


```

Finally, the `representedParty` element is defined.

```xml

```