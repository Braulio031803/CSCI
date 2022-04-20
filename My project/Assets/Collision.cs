using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerCollision : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnCollisionEnter(collision c)
    {
       if (Equals(c.GetComponent<collider>().tag, "wall"))
       {
          // We hit a wall...what should we do?
          // Player take damage.
          // Restart the level.
       }
    }
}
