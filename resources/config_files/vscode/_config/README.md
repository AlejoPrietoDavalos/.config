# Inspeccionar Tokens de VSCode

Para encontrar el scope exacto de un token:

1. **Ctrl+Shift+P** → `Inspect Editor Tokens and Scopes`
2. Clickea sobre el token
3. Copia el scope del resultado en `textmate scopes`

Luego agrega a `template_settings.jsonc` en `textMateRules`:

```jsonc
{
    "scope": "tu.scope.aqui",
    "settings": {
        "foreground": "{{syntax.variables}}"
    }
}
```
